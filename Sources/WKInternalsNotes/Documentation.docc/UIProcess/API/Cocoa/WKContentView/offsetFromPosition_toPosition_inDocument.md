# ``WKInternalsNotes/WKContentView/offsetFromPosition(_:toPosition:inDocument:)``

検索対象ドキュメント内の位置差分を返す。

## Objective-C Declaration
```objective-c
- (NSInteger)offsetFromPosition:(UITextPosition *)from toPosition:(UITextPosition *)toPosition inDocument:(UITextSearchDocumentIdentifier)document;
```

## Discussion
`document` は使用せず、既存の `-offsetFromPosition:toPosition:` に処理を委譲する。

## References
- [`WKContentViewInteraction.h#L986`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L986)
- [`WKContentViewInteraction.mm#L12769`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12769)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
