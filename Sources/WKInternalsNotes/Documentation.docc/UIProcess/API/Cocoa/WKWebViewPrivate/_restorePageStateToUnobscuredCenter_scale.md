# ``WKInternalsNotes/WKWebView/_restorePageStateToUnobscuredCenter(_:scale:)``

`_restorePageStateToUnobscuredCenter` を実行する。

## Objective-C Declaration
```objective-c
- (void)_restorePageStateToUnobscuredCenter:(std::optional<WebCore::FloatPoint>)center scale:(double)scale; // FIXME: needs scroll origin?
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewIOS.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L76)
- [`API/ios/WKWebViewIOS.mm#L1591`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L1591)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
