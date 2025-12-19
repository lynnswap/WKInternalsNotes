# ``WKInternalsNotes/WKContentView/_didHandleDragStartRequest(_:)``

ドラッグ開始要求の完了処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didHandleDragStartRequest:(BOOL)started;
```

## Discussion
開始要求の完了ブロックを呼び出し、ドラッグアイテムが無い場合は状態をクリーンアップする。開始扱いだった場合は `dragstart` と整合するよう `dragend` を送出する。

## References
- [`WKContentViewInteraction.h#L895`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L895)
- [`WKContentViewInteraction.mm#L10652`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10652)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
