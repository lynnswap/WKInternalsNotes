# ``WKInternalsNotes/WKFocusedFormControlView/engageFocusedFormControlNavigation()``

デジタルクラウンによるナビゲーションを開始する。

## Objective-C Declaration
```objective-c
- (void)engageFocusedFormControlNavigation;
```

## Discussion
`PUICCrownInputSequencer` が無ければ生成して各種設定を行い、`scrollViewForFocusedFormControlView:` のオフセットを保存する。シーケンサのオフセットを初期化して delegate を `self` に設定する。

## References
- [`WKFocusedFormControlView.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L62)
- [`WKFocusedFormControlView.mm#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
