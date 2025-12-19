# ``WKInternalsNotes/WKContentView/stopRelinquishingFirstResponderToFocusedElement()``

フォーカス中要素へのレスポンダー移譲を終了する。

## Objective-C Declaration
```objective-c
- (void)stopRelinquishingFirstResponderToFocusedElement;
```

## Discussion
フラグを解除し、`WKWebView` のフォーカス保持カウントを減らす。

## References
- [`WKContentViewInteraction.h#L868`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L868)
- [`WKContentViewInteraction.mm#L9924`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9924)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
