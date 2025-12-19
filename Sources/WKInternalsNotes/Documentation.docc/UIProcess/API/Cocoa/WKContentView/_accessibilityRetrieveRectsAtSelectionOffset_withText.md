# ``WKInternalsNotes/WKContentView/_accessibilityRetrieveRectsAtSelectionOffset(_:withText:)``

選択位置とテキストに基づく矩形取得を開始する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityRetrieveRectsAtSelectionOffset:(NSInteger)offset withText:(NSString *)text;
```

## Discussion
completion handler なしで `_accessibilityRetrieveRectsAtSelectionOffset:withText:completionHandler:` を呼び出す薄いラッパー。

## References
- [WKContentViewInteraction.h#L852](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L852)
- [WKContentViewInteraction.mm#L5084](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5084)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
