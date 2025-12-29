# ``WKInternalsNotes/WKFormAccessoryViewDelegate/accessoryViewDone(_:)``

完了ボタンタップ時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)accessoryViewDone:(WKFormAccessoryView *)view;
```

## Discussion
`WKFormAccessoryView` の `_done` から delegate に通知される。`WKContentViewInteraction` ではフォーカス保持のカウントをリセットしつつログを出し、入力の終了とフォーカス表示更新を行った上で `isShowingInputViewForFocusedElement` を `false` にする。

## References
- [`WKFormAccessoryView.mm#L287`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L287)
- [`WKContentViewInteraction.mm#L6224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6224)
- [`WKFormAccessoryView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
