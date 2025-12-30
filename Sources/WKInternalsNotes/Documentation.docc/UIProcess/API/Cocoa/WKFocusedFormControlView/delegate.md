# ``WKInternalsNotes/WKFocusedFormControlView/delegate``

`WKFocusedFormControlViewDelegate` を弱参照で保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKFocusedFormControlViewDelegate> delegate;
```

## Default Value
`initWithFrame:delegate:` で設定される（未設定なら `nil`）。

## Discussion
getter は `WeakObjCPtr` の値を返し、setter は `_delegate` を更新する。

## References
- [`WKFocusedFormControlView.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L67)
- [`WKFocusedFormControlView.mm#L177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L177)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
