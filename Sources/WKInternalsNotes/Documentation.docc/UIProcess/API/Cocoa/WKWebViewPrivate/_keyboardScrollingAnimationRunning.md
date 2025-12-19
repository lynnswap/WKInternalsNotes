# ``WKInternalsNotes/WKWebView/_keyboardScrollingAnimationRunning``

`_keyboardScrollingAnimationRunning` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isKeyboardScrollingAnimationRunning) BOOL _keyboardScrollingAnimationRunning;
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isKeyboardScrollingAnimationRunning`。

## References
- [`API/ios/WKWebViewPrivateForTestingIOS.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L53)
- [`API/ios/WKWebViewTestingIOS.mm#L408`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L408)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
