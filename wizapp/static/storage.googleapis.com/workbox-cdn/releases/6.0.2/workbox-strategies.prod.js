this.workbox = this.workbox || {}, this.workbox.strategies = function(t, e, s, r, i, n, a, o, c) {
    "use strict";

    function h() {
        return (h = Object.assign || function(t) {
            for (var e = 1; e < arguments.length; e++) {
                var s = arguments[e];
                for (var r in s) Object.prototype.hasOwnProperty.call(s, r) && (t[r] = s[r])
            }
            return t
        }).apply(this, arguments)
    }
    try {
        self["workbox:strategies:6.0.2"] && _()
    } catch (t) {}

    function l(t) {
        return "string" == typeof t ? new Request(t) : t
    }
    class u {
        constructor(t, e) {
            this.vt = {}, Object.assign(this, e), this.event = e.event, this.ht = t, this.bt = new a.Deferred, this._t = [], this.kt = [...t.plugins], this.xt = new Map;
            for (const t of this.kt) this.xt.set(t, {});
            this.event.waitUntil(this.bt.promise)
        }
        fetch(t) {
            return this.waitUntil((async () => {
                const {
                    event: e
                } = this;
                let r = l(t);
                if ("navigate" === r.mode && e instanceof FetchEvent && e.preloadResponse) {
                    const t = await e.preloadResponse;
                    if (t) return t
                }
                const i = this.hasCallback("fetchDidFail") ? r.clone() : null;
                try {
                    for (const t of this.iterateCallbacks("requestWillFetch")) r = await t({
                        request: r.clone(),
                        event: e
                    })
                } catch (t) {
                    throw new s.WorkboxError("plugin-error-request-will-fetch", {
                        thrownError: t
                    })
                }
                const n = r.clone();
                try {
                    let t;
                    t = await fetch(r, "navigate" === r.mode ? void 0 : this.ht.fetchOptions);
                    for (const s of this.iterateCallbacks("fetchDidSucceed")) t = await s({
                        event: e,
                        request: n,
                        response: t
                    });
                    return t
                } catch (t) {
                    throw i && await this.runCallbacks("fetchDidFail", {
                        error: t,
                        event: e,
                        originalRequest: i.clone(),
                        request: n.clone()
                    }), t
                }
            })())
        }
        async fetchAndCachePut(t) {
            const e = await this.fetch(t),
                s = e.clone();
            return this.waitUntil(this.cachePut(t, s)), e
        }
        cacheMatch(t) {
            return this.waitUntil((async () => {
                const e = l(t);
                let s;
                const {
                    cacheName: r,
                    matchOptions: i
                } = this.ht, n = await this.getCacheKey(e, "read"), a = h({}, i, {
                    cacheName: r
                });
                s = await caches.match(n, a);
                for (const t of this.iterateCallbacks("cachedResponseWillBeUsed")) s = await t({
                    cacheName: r,
                    matchOptions: i,
                    cachedResponse: s,
                    request: n,
                    event: this.event
                }) || void 0;
                return s
            })())
        }
        async cachePut(t, e) {
            const r = l(t);
            await c.timeout(0);
            const a = await this.getCacheKey(r, "write");
            if (!e) throw new s.WorkboxError("cache-put-with-no-response", {
                url: i.getFriendlyURL(a.url)
            });
            const h = await this.Rt(e);
            if (!h) return;
            const {
                cacheName: u,
                matchOptions: w
            } = this.ht, f = await self.caches.open(u), d = this.hasCallback("cacheDidUpdate"), p = d ? await n.cacheMatchIgnoreParams(f, a.clone(), ["__WB_REVISION__"], w) : null;
            try {
                await f.put(a, d ? h.clone() : h)
            } catch (t) {
                throw "QuotaExceededError" === t.name && await o.executeQuotaErrorCallbacks(), t
            }
            for (const t of this.iterateCallbacks("cacheDidUpdate")) await t({
                cacheName: u,
                oldResponse: p,
                newResponse: h.clone(),
                request: a,
                event: this.event
            })
        }
        async getCacheKey(t, e) {
            if (!this.vt[e]) {
                let s = t;
                for (const t of this.iterateCallbacks("cacheKeyWillBeUsed")) s = l(await t({
                    mode: e,
                    request: s,
                    event: this.event,
                    params: this.params
                }));
                this.vt[e] = s
            }
            return this.vt[e]
        }
        hasCallback(t) {
            for (const e of this.ht.plugins)
                if (t in e) return !0;
            return !1
        }
        async runCallbacks(t, e) {
            for (const s of this.iterateCallbacks(t)) await s(e)
        }* iterateCallbacks(t) {
            for (const e of this.ht.plugins)
                if ("function" == typeof e[t]) {
                    const s = this.xt.get(e),
                        r = r => {
                            const i = h({}, r, {
                                state: s
                            });
                            return e[t](i)
                        };
                    yield r
                }
        }
        waitUntil(t) {
            return this._t.push(t), t
        }
        async doneWaiting() {
            let t;
            for (; t = this._t.shift();) await t
        }
        destroy() {
            this.bt.resolve()
        }
        async Rt(t) {
            let e = t,
                s = !1;
            for (const t of this.iterateCallbacks("cacheWillUpdate"))
                if (e = await t({
                        request: this.request,
                        response: e,
                        event: this.event
                    }) || void 0, s = !0, !e) break;
            return s || e && 200 !== e.status && (e = void 0), e
        }
    }
    class w {
        constructor(t = {}) {
            this.cacheName = r.cacheNames.getRuntimeName(t.cacheName), this.plugins = t.plugins || [], this.fetchOptions = t.fetchOptions, this.matchOptions = t.matchOptions
        }
        handle(t) {
            const [e] = this.handleAll(t);
            return e
        }
        handleAll(t) {
            t instanceof FetchEvent && (t = {
                event: t,
                request: t.request
            });
            const e = t.event,
                s = "string" == typeof t.request ? new Request(t.request) : t.request,
                r = "params" in t ? t.params : void 0,
                i = new u(this, {
                    event: e,
                    request: s,
                    params: r
                }),
                n = this.Wt(i, s, e);
            return [n, this.Ut(n, i, s, e)]
        }
        async Wt(t, e, r) {
            await t.runCallbacks("handlerWillStart", {
                event: r,
                request: e
            });
            let i = void 0;
            try {
                if (i = await this._handle(e, t), !i || "error" === i.type) throw new s.WorkboxError("no-response", {
                    url: e.url
                })
            } catch (s) {
                for (const n of t.iterateCallbacks("handlerDidError"))
                    if (i = await n({
                            error: s,
                            event: r,
                            request: e
                        }), i) break;
                if (!i) throw s
            }
            for (const s of t.iterateCallbacks("handlerWillRespond")) i = await s({
                event: r,
                request: e,
                response: i
            });
            return i
        }
        async Ut(t, e, s, r) {
            let i, n;
            try {
                i = await t
            } catch (n) {}
            try {
                await e.runCallbacks("handlerDidRespond", {
                    event: r,
                    request: s,
                    response: i
                }), await e.doneWaiting()
            } catch (t) {
                n = t
            }
            if (await e.runCallbacks("handlerDidComplete", {
                    event: r,
                    request: s,
                    response: i,
                    error: n
                }), e.destroy(), n) throw n
        }
    }
    const f = {
        cacheWillUpdate: async ({
            response: t
        }) => 200 === t.status || 0 === t.status ? t : null
    };
    return t.CacheFirst = class extends w {
        async _handle(t, e) {
            let r, i = await e.cacheMatch(t);
            if (!i) try {
                i = await e.fetchAndCachePut(t)
            } catch (t) {
                r = t
            }
            if (!i) throw new s.WorkboxError("no-response", {
                url: t.url,
                error: r
            });
            return i
        }
    }, t.CacheOnly = class extends w {
        async _handle(t, e) {
            const r = await e.cacheMatch(t);
            if (!r) throw new s.WorkboxError("no-response", {
                url: t.url
            });
            return r
        }
    }, t.NetworkFirst = class extends w {
        constructor(t = {}) {
            super(t), this.plugins.some((t => "cacheWillUpdate" in t)) || this.plugins.unshift(f), this.Ct = t.networkTimeoutSeconds || 0
        }
        async _handle(t, e) {
            const r = [],
                i = [];
            let n;
            if (this.Ct) {
                const {
                    id: s,
                    promise: a
                } = this.Dt({
                    request: t,
                    logs: r,
                    handler: e
                });
                n = s, i.push(a)
            }
            const a = this.Et({
                timeoutId: n,
                request: t,
                logs: r,
                handler: e
            });
            i.push(a);
            for (const t of i) e.waitUntil(t);
            let o = await Promise.race(i);
            if (o || (o = await a), !o) throw new s.WorkboxError("no-response", {
                url: t.url
            });
            return o
        }
        Dt({
            request: t,
            logs: e,
            handler: s
        }) {
            let r;
            return {
                promise: new Promise((e => {
                    r = setTimeout((async () => {
                        e(await s.cacheMatch(t))
                    }), 1e3 * this.Ct)
                })),
                id: r
            }
        }
        async Et({
            timeoutId: t,
            request: e,
            logs: s,
            handler: r
        }) {
            let i, n;
            try {
                n = await r.fetchAndCachePut(e)
            } catch (t) {
                i = t
            }
            return t && clearTimeout(t), !i && n || (n = await r.cacheMatch(e)), n
        }
    }, t.NetworkOnly = class extends w {
        constructor(t = {}) {
            super(t), this.Ct = t.networkTimeoutSeconds || 0
        }
        async _handle(t, e) {
            let r, i = void 0;
            try {
                const s = [e.fetch(t)];
                if (this.Ct) {
                    const t = c.timeout(1e3 * this.Ct);
                    s.push(t)
                }
                if (r = await Promise.race(s), !r) throw new Error("Timed out the network response after " + this.Ct + " seconds.")
            } catch (t) {
                i = t
            }
            if (!r) throw new s.WorkboxError("no-response", {
                url: t.url,
                error: i
            });
            return r
        }
    }, t.StaleWhileRevalidate = class extends w {
        constructor(t) {
            super(t), this.plugins.some((t => "cacheWillUpdate" in t)) || this.plugins.unshift(f)
        }
        async _handle(t, e) {
            const r = e.fetchAndCachePut(t).catch((() => {}));
            let i, n = await e.cacheMatch(t);
            if (n);
            else try {
                n = await r
            } catch (t) {
                i = t
            }
            if (!n) throw new s.WorkboxError("no-response", {
                url: t.url,
                error: i
            });
            return n
        }
    }, t.Strategy = w, t.StrategyHandler = u, t
}({}, workbox.core._private, workbox.core._private, workbox.core._private, workbox.core._private, workbox.core._private, workbox.core._private, workbox.core._private, workbox.core._private);
//# sourceMappingURL=workbox-strategies.prod.js.map