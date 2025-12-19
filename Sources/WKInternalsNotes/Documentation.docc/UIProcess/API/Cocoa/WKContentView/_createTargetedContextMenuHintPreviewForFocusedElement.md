# ``WKInternalsNotes/WKContentView/_createTargetedContextMenuHintPreviewForFocusedElement(_:)``

フォーカス中要素向けのコンテキストメニューヒント用プレビューを生成する。

## Objective-C Declaration
```objective-c
- (UITargetedPreview *)_createTargetedContextMenuHintPreviewForFocusedElement:(WebKit::TargetedPreviewPositioning)positioning;
```

## Discussion
フォーカス要素の種別に応じて背景色を決め、`interactionRect` を基にプレビュー矩形を算出する。必要に応じて表示方向と空き領域から矩形を左右どちらかに寄せ、スナップショット由来の `UITargetedPreview` を作成して保持する。

## References
- [`WKContentViewInteraction.h#L957`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L957)
- [`WKContentViewInteraction.mm#L11719`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11719)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
