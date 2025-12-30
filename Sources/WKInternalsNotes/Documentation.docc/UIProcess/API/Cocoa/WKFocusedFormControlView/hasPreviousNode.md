# ``WKInternalsNotes/WKFocusedFormControlView/hasPreviousNode``

前のノードが存在するかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL hasPreviousNode;
```

## Default Value
初期値は `NO`。

## Discussion
`reloadData:` で delegate から取得して更新され、クラウン入力時の遷移判定に使われる。

## References
- [`WKFocusedFormControlView.mm#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L68)
- [`WKFocusedFormControlView.mm#L279`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L279)
- [`WKFocusedFormControlView.mm#L371`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L371)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
