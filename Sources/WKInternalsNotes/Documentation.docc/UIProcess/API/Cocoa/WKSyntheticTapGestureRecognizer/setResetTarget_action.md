# ``WKInternalsNotes/WKSyntheticTapGestureRecognizer/setResetTarget(_:action:)``

reset 時に呼び出す target/action を設定する。

## Objective-C Declaration
```objective-c
- (void)setResetTarget:(id)target action:(SEL)action;
```

## Discussion
`_resetTarget` と `_resetAction` に保存し、`reset` 実行時に呼ばれる。

## References
- [`WKSyntheticTapGestureRecognizer.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.h#L39)
- [`WKSyntheticTapGestureRecognizer.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
