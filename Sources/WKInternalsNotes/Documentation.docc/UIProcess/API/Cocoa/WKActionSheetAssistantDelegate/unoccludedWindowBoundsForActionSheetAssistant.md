# ``WKInternalsNotes/WKActionSheetAssistantDelegate/unoccludedWindowBoundsForActionSheetAssistant(_:)``

被覆されていないウィンドウ領域を返す。

## Objective-C Declaration
```objective-c
- (CGRect)unoccludedWindowBoundsForActionSheetAssistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
`scrollView.adjustedContentInset` を `webView` の `bounds` から差し引いた矩形を作り、ウィンドウ座標へ変換して返す。

## References
- [`WKActionSheetAssistant.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L70)
- [`WKContentViewInteraction.mm#L10076`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10076)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
