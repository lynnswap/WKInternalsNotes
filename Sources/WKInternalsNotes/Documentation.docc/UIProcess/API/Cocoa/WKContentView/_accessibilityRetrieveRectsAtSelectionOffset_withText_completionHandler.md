# ``WKInternalsNotes/WKContentView/_accessibilityRetrieveRectsAtSelectionOffset(_:withText:completionHandler:)``

選択位置とテキストに基づく矩形を取得し、必要ならコールバックする。

## Objective-C Declaration
```objective-c
- (void)_accessibilityRetrieveRectsAtSelectionOffset:(NSInteger)offset withText:(NSString *)text completionHandler:(void (^)(const Vector<WebCore::SelectionGeometry>& rects))completionHandler;
```

## Discussion
`_page->requestRectsAtSelectionOffsetWithText` を呼び、結果を completion handler に渡した後 `_accessibilityDidGetSelectionRects:withGranularity:atOffset:` を `UITextGranularityWord` で通知する。

## References
- [WKContentViewInteraction.h#L851](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L851)
- [WKContentViewInteraction.mm#L5089](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5089)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
