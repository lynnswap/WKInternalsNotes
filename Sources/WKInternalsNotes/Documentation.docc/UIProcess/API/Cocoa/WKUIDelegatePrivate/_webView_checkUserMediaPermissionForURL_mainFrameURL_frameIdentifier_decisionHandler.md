# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:checkUserMediaPermissionForURL:mainFrameURL:frameIdentifier:decisionHandler:)``

ユーザメディア許可判定の delegate フック（現在は呼び出されない）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView checkUserMediaPermissionForURL:(NSURL *)url mainFrameURL:(NSURL *)mainFrameURL frameIdentifier:(NSUInteger)frameIdentifier decisionHandler:(void (^)(NSString *salt, BOOL authorized))decisionHandler WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Discussion
ヘッダに「This delegate is no longer called.」と記載されており、UIProcess 内の呼び出しも見当たらない。

## References
- [`WKUIDelegatePrivate.h#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
