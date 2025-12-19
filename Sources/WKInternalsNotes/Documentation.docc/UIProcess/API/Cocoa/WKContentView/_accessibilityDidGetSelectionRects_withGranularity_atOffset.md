# ``WKInternalsNotes/WKContentView/_accessibilityDidGetSelectionRects(_:withGranularity:atOffset:)``

選択矩形取得の結果を通知する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityDidGetSelectionRects:(NSArray *)selectionRects withGranularity:(UITextGranularity)granularity atOffset:(NSInteger)offset;
```

## Discussion
`_accessibilityRetrieveRectsEnclosingSelectionOffset:withGranularity:` などが取得した矩形を渡すコールバックとして利用される。

## References
- [`WKContentViewInteraction.mm#L1144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1144)
- [`WKContentViewInteraction.mm#L5079`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5079)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
