# ``WKInternalsNotes/WKWebView/_keyboardWillChangeFrame(_:)``

`_keyboardWillChangeFrame` を実行する。

## Objective-C Declaration
```objective-c
- (void)_keyboardWillChangeFrame:(NSNotification *)notification;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L46)
- [`WKWebViewIOS.mm#L3470`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3470)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
