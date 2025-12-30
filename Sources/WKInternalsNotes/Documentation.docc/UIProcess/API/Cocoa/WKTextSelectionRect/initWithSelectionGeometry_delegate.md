# ``WKInternalsNotes/WKTextSelectionRect/initWithSelectionGeometry(_:delegate:)``

選択ジオメトリとデリゲートで初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSelectionGeometry:(const WebCore::SelectionGeometry&)selectionGeometry delegate:(id<WKTextSelectionRectDelegate>)delegate;
```

## Discussion
`[super init]` に成功した場合、`_selectionGeometry` と `_delegate` を設定して返す。初期化に失敗した場合は `nil` を返す。

## References
- [`WKTextSelectionRect.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextSelectionRect.h#L53)
- [`WKTextSelectionRect.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextSelectionRect.mm#L93)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
