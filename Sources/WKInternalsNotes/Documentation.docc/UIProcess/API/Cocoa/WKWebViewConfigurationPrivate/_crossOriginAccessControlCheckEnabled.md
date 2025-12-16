# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_crossOriginAccessControlCheckEnabled``

CORS の access control check を有効/無効にする

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCrossOriginAccessControlCheckEnabled:) BOOL _crossOriginAccessControlCheckEnabled WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_crossOriginAccessControlCheckEnabled = YES`: CORS の access control check を通常どおり行う。
- `_crossOriginAccessControlCheckEnabled = NO`: WebContent process 内の `CrossOriginAccessControlCheckDisabler` を通じてチェックを緩和する（例: credentials が有効でも `Access-Control-Allow-Origin: *` を許容する）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L105)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1158)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WebKit/WebProcess/WebPage/WebPage.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebPage.cpp)
- [`Source/WebCore/loader/CrossOriginAccessControl.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/CrossOriginAccessControl.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
