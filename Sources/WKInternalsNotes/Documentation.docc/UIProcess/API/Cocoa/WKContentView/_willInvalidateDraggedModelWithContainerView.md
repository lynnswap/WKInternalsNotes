# ``WKInternalsNotes/WKContentView/_willInvalidateDraggedModelWithContainerView(_:)``

ドラッグ中のモデルビューが破棄される前の処理を行う。

## Objective-C Declaration
```objective-c
- (void)_willInvalidateDraggedModelWithContainerView:(UIView *)containerView;
```

## Discussion
ドラッグ中にモデルが破棄される場合、プレビュー用コンテナへ移してウィンドウ内に残しつつ非表示にする。

## References
- [`WKContentViewInteraction.h#L1022`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1022)
- [`WKContentViewInteraction.mm#L14339`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14339)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
