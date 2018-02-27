namespace py headless_render

struct Request {
    1: required string url; //需要爬取的url
    2: required i64 ad_id;
}

exception RenderFailedException {
    1: required i32 code;
    2: optional string message;
}

service HeadlessRenderService {
    string getRenderHtml(1: Request request) throws (1: RenderFailedException excpetion);
}