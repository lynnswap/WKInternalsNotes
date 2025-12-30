# ``WKInternalsNotes/WKFocusedFormControlView/disengageFocusedFormControlNavigation()``

デジタルクラウンによるナビゲーションを終了する。

## Objective-C Declaration
```objective-c
- (void)disengageFocusedFormControlNavigation;
```

## Discussion
保留中の更新をキャンセルし、シーケンサの減速を停止してオフセットを 0 に戻し、delegate を `nil` にする。

## References
- [`WKFocusedFormControlView.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L63)
- [`WKFocusedFormControlView.mm#L247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L247)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
