# ``WKInternalsNotes/WKContentView/shouldHideSelectionInFixedPositionWhenScrolling``

固定位置要素内の選択をスクロール時に隠すべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL shouldHideSelectionInFixedPositionWhenScrolling;
```

## Default Value
編集状態や editorState の固定位置情報に依存して判定する。

## Discussion
`selectionHonorsOverflowScrolling` が有効なら `NO`。編集時は `_focusedElementInformation.insideFixedPosition`、それ以外は `editorState` の post-layout 情報を参照して判定する。

## References
- [`WKContentViewInteraction.h#L722`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L722)
- [`WKContentViewInteraction.mm#L1936`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1936)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
