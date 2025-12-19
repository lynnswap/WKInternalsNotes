# ``WKInternalsNotes/WKTextInteractionWrapper/willBeginDragLift()``

ドラッグ開始時に選択/編集メニューを一時的に隠す。

## Objective-C Declaration
```objective-c
- (void)willBeginDragLift;
```

## Discussion
既に `HideEditMenuScope` がある場合や context menu が表示中の場合は何もしない。そうでなければ `HideEditMenuScope` を作成し、選択を非アクティブ化しつつ edit menu を抑制する。

## References
- [`WKTextInteractionWrapper.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L61)
- [`WKTextInteractionWrapper.mm#L337`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L337)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
