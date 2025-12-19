# ``WKInternalsNotes/WKWebView/_corsDisablingPatterns``

`_corsDisablingPatterns` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCORSDisablingPatterns:) NSArray<NSString *> *_corsDisablingPatterns WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setCORSDisablingPatterns:`。

## References
- [`WKWebViewPrivate.h#L266`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L266)
- [`WKWebView.mm#L5281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5281)
- [`WKWebView.mm#L5281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5281)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
