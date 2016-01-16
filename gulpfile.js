/*jslint indent:4, node:true, sloppy:true*/

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer');
    /* TODO: add watch, browserSync, imgmin, ... */

gulp.task('img', function () {
    gulp.src('./mindsurf/static_dev/img/*')
        .pipe(gulp.dest('./mindsurf/static/img'));
});

gulp.task('js', function () {
    gulp.src('./mindsurf/static_dev/js/*.js')
        .pipe(gulp.dest('./mindsurf/static/js'));
});

gulp.task('sass', function () {
    gulp.src("./mindsurf/static_dev/sass/style.scss")
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(gulp.dest('./mindsurf/static/css'));
});

gulp.task('normalize', function () {
    gulp.src('./bower_components/normalize.css/normalize.css')
        .pipe(gulp.dest('./mindsurf/static/css'));
});

gulp.task('outdated-browser-css', function () {
    gulp.src('./bower_components/outdated-browser/outdatedbrowser/outdatedbrowser.min.css')
        .pipe(gulp.dest('./mindsurf/static/css'));
});

gulp.task('outdated-browser-js', function () {
    gulp.src('./bower_components/outdated-browser/outdatedbrowser/outdatedbrowser.min.js')
        .pipe(gulp.dest('./mindsurf/static/js'));
});

gulp.task('outdated-browser-lang', function () {
    gulp.src('./bower_components/outdated-browser/outdatedbrowser/lang/ru.html')
        .pipe(gulp.dest('./mindsurf/static/js/lang'));
});

gulp.task('bower', [
    'normalize',
    'outdated-browser-css',
    'outdated-browser-js'
    //TODO: 'outdated-browser-lang'   
]);

gulp.task('watch', ['sass', 'js'], function () {
    gulp.watch("./mindsurf/static_dev/sass/**/*.scss", ['sass']);
    gulp.watch("./mindsurf/static_dev/js/**/*.js", ['js']);
});

gulp.task('default', ['img', 'sass', 'js', 'bower']);
