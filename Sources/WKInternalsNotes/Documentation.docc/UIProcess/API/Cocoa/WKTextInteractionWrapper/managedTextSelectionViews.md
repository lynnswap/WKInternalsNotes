# ``WKInternalsNotes/WKTextInteractionWrapper/managedTextSelectionViews``

管理下の選択表示ビューを配列で返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<UIView *> *managedTextSelectionViews;
```

## Default Value
初期は空。`prepareToMoveSelectionContainer:` で更新される。

## Discussion
弱参照で保持している `_managedTextSelectionViews` を走査し、解放済みのビューを除外して配列化する。

## References
- [`WKTextInteractionWrapper.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L71)
- [`WKTextInteractionWrapper.mm#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L180)
- [`WKTextInteractionWrapper.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
