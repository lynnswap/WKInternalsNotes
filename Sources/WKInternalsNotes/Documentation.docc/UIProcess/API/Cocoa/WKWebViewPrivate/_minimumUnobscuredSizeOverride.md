# ``WKInternalsNotes/WKWebView/_minimumUnobscuredSizeOverride``

`_minimumUnobscuredSizeOverride` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize _minimumUnobscuredSizeOverride WK_API_AVAILABLE(ios(17.4), visionos(1.1));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L695`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L695)
- [`WKWebViewIOS.mm#L4304`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4304)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
