!function(n){woodmartThemeModule.$document.on("wdCloseMobileMenu",function(){woodmartThemeModule.closeMobileNavigation()}),woodmartThemeModule.mobileNavigation=function(){var e=woodmartThemeModule.$body,o=n(".mobile-nav"),d=n(".mobile-nav .wd-nav-mobile .menu-item-has-children"),a=n(".wd-close-side");d.append('<span class="wd-nav-opener"></span>'),o.on("click",".wd-nav-opener",function(e){e.preventDefault();e=n(this).parent();e.hasClass("opener-page")?(e.removeClass("opener-page").find("> ul, > .wd-sub-menu").slideUp(200),e.removeClass("opener-page").find(".wd-dropdown-menu .container > ul, .wd-dropdown-menu > ul").slideUp(200),e.find("> .wd-nav-opener").removeClass("wd-active")):(e.addClass("opener-page").find("> ul, > .wd-sub-menu").slideDown(200),e.addClass("opener-page").find(".wd-dropdown-menu .container > ul, .wd-dropdown-menu > ul").slideDown(200),e.find("> .wd-nav-opener").addClass("wd-active")),woodmartThemeModule.$document.trigger("wood-images-loaded")}),o.on("click",".wd-nav-mob-tab li",function(e){e.preventDefault();var e=n(this),o=e.data("menu");e.hasClass("wd-active")||(e.parent().find(".wd-active").removeClass("wd-active"),e.addClass("wd-active"),n(".wd-nav-mobile").removeClass("wd-active"),n(".mobile-"+o+"-menu").addClass("wd-active"),woodmartThemeModule.$document.trigger("wood-images-loaded"))}),e.on("click",".wd-header-mobile-nav > a",function(e){e.preventDefault(),o.hasClass("wd-opened")?woodmartThemeModule.closeMobileNavigation():(n(this).parent().addClass("wd-opened"),o.addClass("wd-opened"),a.addClass("wd-close-side-opened"),woodmartThemeModule.$document.trigger("wood-images-loaded"))}),e.on("click touchstart",".wd-close-side",function(e){e.preventDefault(),woodmartThemeModule.closeMobileNavigation()}),e.on("click",".mobile-nav .login-side-opener, .mobile-nav .close-side-widget",function(e){e.preventDefault(),woodmartThemeModule.closeMobileNavigation()})},woodmartThemeModule.closeMobileNavigation=function(){n(".wd-header-mobile-nav").removeClass("wd-opened"),n(".mobile-nav").removeClass("wd-opened"),n(".wd-close-side").removeClass("wd-close-side-opened"),n(".mobile-nav .searchform input[type=text]").blur()},n(document).ready(function(){woodmartThemeModule.mobileNavigation()})}(jQuery);