this.workbox = this.workbox || {}, this.workbox.core = function(t) {
    "use strict";
    try {
        self["workbox:core:6.0.2"] && _()
    } catch (t) {}
    const e = (t, ...e) => {
        let n = t;
        return e.length > 0 && (n += " :: " + JSON.stringify(e)), n
    };
    class n extends Error {
        constructor(t, n) {
            super(e(t, n)), this.name = t, this.details = n
        }
    }
    const r = new Set;
    const s = {
            googleAnalytics: "googleAnalytics",
            precache: "precache-v2",
            prefix: "workbox",
            runtime: "runtime",
            suffix: "undefined" != typeof registration ? registration.scope : ""
        },
        o = t => [s.prefix, t, s.suffix].filter((t => t && t.length > 0)).join("-"),
        i = {
            updateDetails: t => {
                (t => {
                    for (const e of Object.keys(s)) t(e)
                })((e => {
                    "string" == typeof t[e] && (s[e] = t[e])
                }))
            },
            getGoogleAnalyticsName: t => t || o(s.googleAnalytics),
            getPrecacheName: t => t || o(s.precache),
            getPrefix: () => s.prefix,
            getRuntimeName: t => t || o(s.runtime),
            getSuffix: () => s.suffix
        };

    function c() {
        return (c = Object.assign || function(t) {
            for (var e = 1; e < arguments.length; e++) {
                var n = arguments[e];
                for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (t[r] = n[r])
            }
            return t
        }).apply(this, arguments)
    }

    function a(t, e) {
        const n = new URL(t);
        for (const t of e) n.searchParams.delete(t);
        return n.href
    }
    let u, l;

    function f() {
        if (void 0 === l) {
            const t = new Response("");
            if ("body" in t) try {
                new Response(t.body), l = !0
            } catch (t) {
                l = !1
            }
            l = !1
        }
        return l
    }
    class h {
        constructor(t, e, {
            onupgradeneeded: n,
            onversionchange: r
        } = {}) {
            this.i = null, this.m = t, this.P = e, this.K = n, this.N = r || (() => this.close())
        }
        get db() {
            return this.i
        }
        async open() {
            if (!this.i) return this.i = await new Promise(((t, e) => {
                let n = !1;
                setTimeout((() => {
                    n = !0, e(new Error("The open request was blocked and timed out"))
                }), this.OPEN_TIMEOUT);
                const r = indexedDB.open(this.m, this.P);
                r.onerror = () => e(r.error), r.onupgradeneeded = t => {
                    n ? (r.transaction.abort(), r.result.close()) : "function" == typeof this.K && this.K(t)
                }, r.onsuccess = () => {
                    const e = r.result;
                    n ? e.close() : (e.onversionchange = this.N.bind(this), t(e))
                }
            })), this
        }
        async getKey(t, e) {
            return (await this.getAllKeys(t, e, 1))[0]
        }
        async getAll(t, e, n) {
            return await this.getAllMatching(t, {
                query: e,
                count: n
            })
        }
        async getAllKeys(t, e, n) {
            return (await this.getAllMatching(t, {
                query: e,
                count: n,
                includeKeys: !0
            })).map((t => t.key))
        }
        async getAllMatching(t, {
            index: e,
            query: n = null,
            direction: r = "next",
            count: s,
            includeKeys: o = !1
        } = {}) {
            return await this.transaction([t], "readonly", ((i, c) => {
                const a = i.objectStore(t),
                    u = e ? a.index(e) : a,
                    l = [],
                    f = u.openCursor(n, r);
                f.onsuccess = () => {
                    const t = f.result;
                    t ? (l.push(o ? t : t.value), s && l.length >= s ? c(l) : t.continue()) : c(l)
                }
            }))
        }
        async transaction(t, e, n) {
            return await this.open(), await new Promise(((r, s) => {
                const o = this.i.transaction(t, e);
                o.onabort = () => s(o.error), o.oncomplete = () => r(), n(o, (t => r(t)))
            }))
        }
        async L(t, e, n, ...r) {
            return await this.transaction([e], n, ((n, s) => {
                const o = n.objectStore(e),
                    i = o[t].apply(o, r);
                i.onsuccess = () => s(i.result)
            }))
        }
        close() {
            this.i && (this.i.close(), this.i = null)
        }
    }
    h.prototype.OPEN_TIMEOUT = 2e3;
    const w = {
        readonly: ["get", "count", "getKey", "getAll", "getAllKeys"],
        readwrite: ["add", "put", "clear", "delete"]
    };
    for (const [t, e] of Object.entries(w))
        for (const n of e) n in IDBObjectStore.prototype && (h.prototype[n] = async function(e, ...r) {
            return await this.L(n, e, t, ...r)
        });

    function g(t) {
        return new Promise((e => setTimeout(e, t)))
    }
    var d = Object.freeze({
        __proto__: null,
        assert: null,
        cacheMatchIgnoreParams: async function(t, e, n, r) {
            const s = a(e.url, n);
            if (e.url === s) return t.match(e, r);
            const o = c({}, r, {
                    ignoreSearch: !0
                }),
                i = await t.keys(e, o);
            for (const e of i) {
                if (s === a(e.url, n)) return t.match(e, r)
            }
        },
        cacheNames: i,
        canConstructReadableStream: function() {
            if (void 0 === u) try {
                new ReadableStream({
                    start() {}
                }), u = !0
            } catch (t) {
                u = !1
            }
            return u
        },
        canConstructResponseFromBodyStream: f,
        dontWaitFor: function(t) {
            t.then((() => {}))
        },
        DBWrapper: h,
        Deferred: class {
            constructor() {
                this.promise = new Promise(((t, e) => {
                    this.resolve = t, this.reject = e
                }))
            }
        },
        deleteDatabase: async t => {
            await new Promise(((e, n) => {
                const r = indexedDB.deleteDatabase(t);
                r.onerror = () => {
                    n(r.error)
                }, r.onblocked = () => {
                    n(new Error("Delete blocked"))
                }, r.onsuccess = () => {
                    e()
                }
            }))
        },
        executeQuotaErrorCallbacks: async function() {
            for (const t of r) await t()
        },
        getFriendlyURL: t => new URL(String(t), location.href).href.replace(new RegExp("^" + location.origin), ""),
        logger: null,
        resultingClientExists: async function(t) {
            if (!t) return;
            let e = await self.clients.matchAll({
                type: "window"
            });
            const n = new Set(e.map((t => t.id)));
            let r;
            const s = performance.now();
            for (; performance.now() - s < 2e3 && (e = await self.clients.matchAll({
                    type: "window"
                }), r = e.find((e => t ? e.id === t : !n.has(e.id))), !r);) await g(100);
            return r
        },
        timeout: g,
        waitUntil: function(t, e) {
            const n = e();
            return t.waitUntil(n), n
        },
        WorkboxError: n
    });
    const y = {
        get googleAnalytics() {
            return i.getGoogleAnalyticsName()
        },
        get precache() {
            return i.getPrecacheName()
        },
        get prefix() {
            return i.getPrefix()
        },
        get runtime() {
            return i.getRuntimeName()
        },
        get suffix() {
            return i.getSuffix()
        }
    };
    return t._private = d, t.cacheNames = y, t.clientsClaim = function() {
        self.addEventListener("activate", (() => self.clients.claim()))
    }, t.copyResponse = async function(t, e) {
        let r = null;
        if (t.url) {
            r = new URL(t.url).origin
        }
        if (r !== self.location.origin) throw new n("cross-origin-copy-response", {
            origin: r
        });
        const s = t.clone(),
            o = {
                headers: new Headers(s.headers),
                status: s.status,
                statusText: s.statusText
            },
            i = e ? e(o) : o,
            c = f() ? s.body : await s.blob();
        return new Response(c, i)
    }, t.registerQuotaErrorCallback = function(t) {
        r.add(t)
    }, t.setCacheNameDetails = function(t) {
        i.updateDetails(t)
    }, t.skipWaiting = function() {
        self.skipWaiting()
    }, t
}({});
//# sourceMappingURL=workbox-core.prod.js.map