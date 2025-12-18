# ``WKInternalsNotes/WKURLSchemeTaskPrivate/_willPerformRedirection(_:newRequest:completionHandler:)``

リダイレクト前に新しいリクエストを URL scheme task に提示する。

## Objective-C Declaration
```objective-c
- (void)_willPerformRedirection:(NSURLResponse *)response newRequest:(NSURLRequest *)request completionHandler:(void (^)(NSURLRequest *))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WebURLSchemeTask::willPerformRedirection` を呼び出し、結果の `ResourceRequest` を `NSURLRequest` に変換して completion handler へ返す。

## References
- [`WKURLSchemeTaskPrivate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTaskPrivate.h#L46)
- [`WKURLSchemeTask.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTask.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
