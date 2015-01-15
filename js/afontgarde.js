/*! afontgarde - v0.1.0 - 2013-12-20
* https://github.com/filamentgroup/a-font-garde
* Copyright (c) 2013 Filament Group c/o Zach Leatherman
* Licensed MIT */

/*
 * Font-Face Onload Script
 */
;(function( win, doc ) {
    var DELAY = 100,
        TEST_STRING = 'AxmTYklsjo190QW',
        TOLERANCE = 2, // px

        SANS_SERIF_FONTS = 'sans-serif',
        SERIF_FONTS = 'serif',

        parent = doc.createElement( 'div' ),
        html = '<div style="font-family:%s;position:absolute;top:0;left:-9999px;font-size:48px">' + TEST_STRING + '</div>',
        sansSerif,
        serif,
        dimensions,
        appended = false;

    parent.innerHTML = html.replace(/\%s/, SANS_SERIF_FONTS ) + html.replace(/\%s/, SERIF_FONTS );
    sansSerif = parent.firstChild;
    serif = sansSerif.nextSibling;

    // intentional global
    FontFaceOnload = function( fontFamily, options ) {
        var defaultOptions = {
                glyphs: '',
                success: function() {},
                error: function() {},
                timeout: 10000
            },
            startTime = new Date();

        if( options ) {
            for( var j in options ) {
                if( options.hasOwnProperty( j ) ) {
                    defaultOptions[ j ] = options[ j ];
                }
            }
        }

        if( options.glyphs ) {
            sansSerif.innerHTML += options.glyphs;
            serif.innerHTML += options.glyphs;
        }

        if( !appended && doc.body ) {
            appended = true;
            doc.body.appendChild( parent );
            dimensions = {
                sansSerif: {
                    width: sansSerif.offsetWidth,
                    height: sansSerif.offsetHeight
                },
                serif: {
                    width: serif.offsetWidth,
                    height: serif.offsetHeight
                }
            };
        }

        // Make sure we set the new font-family after we take our initial dimensions:
        // handles the case where FontFaceOnload is called after the font has already
        // loaded.
        sansSerif.style.fontFamily = fontFamily + ', ' + SANS_SERIF_FONTS;
        serif.style.fontFamily = fontFamily + ', ' + SERIF_FONTS;

        (function checkDimensions() {
            if( Math.abs( dimensions.sansSerif.width - sansSerif.offsetWidth ) > TOLERANCE ||
                Math.abs( dimensions.sansSerif.height - sansSerif.offsetHeight ) > TOLERANCE ||
                Math.abs( dimensions.serif.width - serif.offsetWidth ) > TOLERANCE ||
                Math.abs( dimensions.serif.height - serif.offsetHeight ) > TOLERANCE ) {

                options.success();
            } else if( ( new Date() ).getTime() - startTime.getTime() > options.timeout ) {
                options.error();
            } else {
                setTimeout(function() {
                    checkDimensions();
                }, DELAY);
            }
        })();
    };
})( this, this.document );


/*
 * A Font Garde
 */
;(function( w ) {

    var doc = w.document,
        ref,
        css = ['.supports-fontface.supports-generatedcontent.%s .icon-fallback-text .icon { display: inline-block; }',
            '.supports-fontface.supports-generatedcontent.%s .icon-fallback-text .text { clip: rect(0 0 0 0); overflow: hidden; position: absolute; height: 1px; width: 1px; }',
            '.supports-fontface.%s .icon-fallback-glyph .icon:before { font-size: inherit; line-height: inherit; }'];

    function addEvent( type, callback ) {
        if( 'addEventListener' in w ) {
            return w.addEventListener( type, callback, false );
        } else if( 'attachEvent' in w ) {
            return w.attachEvent( 'on' + type, callback );
        }
    }

    AFontGarde = function( fontFamily, sampleGlyphs ) {
        var executed = false;
        function init() {
            if( executed ) {
                return;
            }
            executed = true;

            if( typeof FontFaceOnload === 'undefined' ) {
                throw 'FontFaceOnload is a prerequisite.';
            }

            if( !ref ) {
                ref = doc.getElementsByTagName( 'script' )[ 0 ];
            }
            var style = doc.createElement( 'style' );
            style.innerHTML = css.join( '\n' ).replace( /\%s/gi, fontFamily );
            ref.parentNode.insertBefore( style, ref );

            FontFaceOnload( fontFamily, {
                // These characters are a few of the glyphs from the font above */
                glyphs: sampleGlyphs || '',
                timeout: 5000,
                success: function() {
                    // If you're using more than one icon font, change this classname (and in a-font-garde.css)
                    doc.documentElement.className += ' ' + fontFamily;
                }
            });
        }

        // MIT credit: filamentgroup/shoestring
        addEvent( "DOMContentLoaded", init );
        addEvent( "readystatechange", init );
        addEvent( "load", init );

        if( doc.readyState === "complete" ){
            init();
        }
    };

})( this );
