odoo.define('website_blog_related_post.related_post_js', function (require) {
'use strict';

   var core = require('web.core');

   const dom = require('web.dom');
   const publicWidget = require('web.public.widget');

   console.log('GET RELATED POST');

   publicWidget.registry.websiteBlogRelated = publicWidget.Widget.extend({
       selector : '.js_get_this_posts',

       /**
       * @override
       */
       start: function () {
          var self = this;
          var blogID = self.$target[0].id;

          this._rpc({
            route: '/blog/render_related_posts',
            params: {
                template: '',
                domain: [],
                limit: 3,
                id: parseInt(blogID)
            },
          }).then(function (posts) {
            for(var i=0; i < posts.posts.length; i++){
              console.log(posts.posts[i]);
              var s = '<div class="col-12 col-md-4 media s_latest_posts_post" style="opacity:0.8;">\
                                                 <div class="media-body ml-3 pb-2 w-100">\
                                                    <h5>\
                                                      <a href="/blog/' + posts.posts[i].blog_id + '/post/' + posts.posts[i].id + '">\
                                                        <span class="text-truncate d-block">' + posts.posts[i].name  + '<span>\
                                                      </a>\
                                                    </h5>\
                                                    <p class="text-blog-related">' + posts.posts[i].teaser + '</p>
                                                    <a class="btn btn-primary" href="/blog/' + posts.posts[i].blog_id + '/post/' + posts.posts[i].id + '">Seguir leyendo</a>\
                                                  </div>\
                                              </div>';
              $('.js_get_this_posts').append(s);
            }
          });
       },
   });
});

