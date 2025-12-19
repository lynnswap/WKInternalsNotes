# ``WKInternalsNotes/WKContentView/canBecomeFirstResponderForWebView()``

WebView の first responder になれるかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)canBecomeFirstResponderForWebView;
```

## Discussion
`_resigningFirstResponder` 中でなければ `YES` を返す。

## References
- [`WKContentViewInteraction.h#L757`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L757)
- [`WKContentViewInteraction.mm#L1987`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1987)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
