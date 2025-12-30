# ``WKInternalsNotes/WKFocusedFormControlView/handleWheelEvent(_:)``

ホイールイベントを処理して `YES` を返す。

## Objective-C Declaration
```objective-c
- (BOOL)handleWheelEvent:(UIEvent *)event;
```

## Discussion
`_wheelChangedWithEvent:` を呼び出した後に `YES` を返す。

## References
- [`WKFocusedFormControlView.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L65)
- [`WKFocusedFormControlView.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
