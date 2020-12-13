const { series, parallel, src,
        pipe, dest } = require('gulp');

const concat = require('gulp-concat'),
      uglify = require('gulp-uglify'),
      cleanCSS = require('gulp-clean-css'),
      rename = require('gulp-rename'),
      clean = require('gulp-clean'),
      watch = require('gulp-watch'),
      plumber = require('gulp-plumber');

var sass = require('gulp-sass');
sass.compiler  = require('node-sass');

// Target Dirs
const templatesDestDir = './prelude_django_admin_toolkit/templates'
const assetsDestDir = './prelude_django_admin_toolkit/static/prelude_django_admin_toolkit'
const sourceDir = 'frontend'

/*
 * Cleanup Functions
 */
function cleanWS() {
    return src(`${assetsDestDir}/*`)
        .pipe(clean());
}

function cleanTemplatesWS() {
    return src(`${templatesDestDir}/*`)
		.pipe(clean());
}

/*
 * Build Functions
 */
function buildSass() {
    return src(`${sourceDir}/scss/*.scss`)
        .pipe(
            sass({
                includePaths: ['./node_modules/']
            }).on('error', sass.logError))
        .pipe(dest(`${assetsDestDir}/css`));
}

function watchSass() {
    return src(`${sourceDir}/scss/*.scss`)
        .pipe(watch(`${sourceDir}/scss/*.scss`))
        .pipe(plumber())
        .pipe(
            sass({
                includePaths: ['./node_modules/']
            }).on('error', sass.logError))
        .pipe(dest(`${assetsDestDir}/css`));
}

function slimCSS() {
    return src(`${assetsDestDir}/css/*.css`)
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(dest(`${assetsDestDir}/css`));
}

function buildJSVendor() {
    let vendorFiles = [
        './node_modules/jquery/dist/jquery.js',
        './node_modules/uikit/dist/js/uikit.js',
        './node_modules/uikit/dist/js/uikit-icons.js'
    ]

    return src(vendorFiles)
        .pipe(concat('vendor.js'))
        .pipe(dest(`${assetsDestDir}/js`));
}

function buildJSApp() {
    return src(`${sourceDir}/js/**/*.js`)
        .pipe(dest(`${assetsDestDir}/js`));
}

function watchJSApp() {
    return src(`${sourceDir}/js/**/*.js`)
        .pipe(watch(`${sourceDir}/js/**/*.js`))
        .pipe(plumber())
        .pipe(dest(`${assetsDestDir}/js`));
}

function buildHTMLTemplates() {
    return src(`${sourceDir}/django_templates/**/*.html`)
        .pipe(dest(templatesDestDir));
}

function buildNormalizeCSS() {
    return src('./node_modules/normalize.css/normalize.css')
        .pipe(dest(`${assetsDestDir}/css`));
}

function buildIcons() {
    return src(`${sourceDir}/icon/**/*`)
        .pipe(dest(`${assetsDestDir}/icon`));
}


function watchHTMLTemplates() {
    return src(`${sourceDir}/django_templates/**/*.html`)
        .pipe(watch(`${sourceDir}/django_templates/**/*.html`))
        .pipe(plumber())
        .pipe(dest(templatesDestDir));
}

function uglifyJS() {
    return src(`${assetsDestDir}/js/**/*.js`)
        .pipe(uglify())
        .pipe(dest(`${assetsDestDir}/js`));
}

// Actions declared
exports.clean = series(cleanWS);

exports.build_dev = series(
    cleanWS,
    buildIcons,
    parallel(
        series(buildNormalizeCSS, buildSass, slimCSS),
        series(buildJSVendor, buildJSApp),
        series(buildHTMLTemplates)
    )
);

exports.build_production = series(
    cleanWS,
    buildIcons,
    parallel(
        series(buildHTMLTemplates),
        series(buildJSVendor, buildJSApp, uglifyJS),
        series(buildNormalizeCSS, buildSass, slimCSS)
    )
);

exports.watch = series(
    cleanWS,
    buildNormalizeCSS,
    buildIcons,
    parallel(
        watchSass,
        series(buildJSVendor, watchJSApp),
        watchHTMLTemplates
    )
);
