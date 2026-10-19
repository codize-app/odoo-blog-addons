import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

export class RelatedPost extends Interaction {
    static selector = ".js_get_this_posts";

    async start() {
        const blogId = parseInt(this.el.id);
        const data = await this.waitFor(
            rpc("/blog/render_related_posts", {
                limit: 3,
                id: blogId,
            })
        );
        for (const post of data.posts) {
            const s = '<div class="col-12 col-md-4 media s_latest_posts_post" style="opacity:0.8;">\
                                                <div class="media-body ml-3 pb-2 w-100">\
                                                   <h5>\
                                                     <a href="/blog/' + post.blog_id + '/post/' + post.id + '">\
                                                       <span class="text-truncate d-block">' + post.name + '<span>\
                                                     </a>\
                                                   </h5>\
                                                   <p class="text-blog-related">' + post.teaser + '</p>\
                                                   <a class="btn btn-primary" href="/blog/' + post.blog_id + '/post/' + post.id + '">Seguir leyendo</a>\
                                                 </div>\
                                             </div>';
            this.el.insertAdjacentHTML("beforeend", s);
        }
    }
}

registry.category("public.interactions").add("website_blog_related_post.related_post", RelatedPost);
