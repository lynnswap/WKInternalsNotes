# ``WKInternalsNotes/WKContentView/startRelinquishingFirstResponderToFocusedElement()``

フォーカス中要素へのレスポンダー移譲を開始する。

## Objective-C Declaration
```objective-c
- (void)startRelinquishingFirstResponderToFocusedElement;
```

## Discussion
二重開始を防ぎつつ `_isRelinquishingFirstResponderToFocusedElement` を立て、`WKWebView` のフォーカス保持カウントを増やす。

## References
- [`WKContentViewInteraction.h#L867`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L867)
- [`WKContentViewInteraction.mm#L9915`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9915)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
