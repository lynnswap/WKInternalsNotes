# ``WKInternalsNotes/WKContentView/_accessibilityRetrieveRectsEnclosingSelectionOffset(_:withGranularity:)``

選択範囲を包む矩形を granularity 単位で取得する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityRetrieveRectsEnclosingSelectionOffset:(NSInteger)offset withGranularity:(UITextGranularity)granularity;
```

## Discussion
`_page->requestRectsForGranularityWithSelectionOffset` を呼び、取得した `SelectionGeometry` を `webSelectionRectsForSelectionGeometries` で変換して `_accessibilityDidGetSelectionRects:withGranularity:atOffset:` に通知する。

## References
- [WKContentViewInteraction.h#L850](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L850)
- [WKContentViewInteraction.mm#L5076](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5076)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
