# ``WKInternalsNotes/WKFocusedFormControlView/hasNextNode``

次のノードが存在するかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL hasNextNode;
```

## Default Value
初期値は `NO`。

## Discussion
`reloadData:` で delegate から取得して更新され、クラウン入力時の遷移判定に使われる。

## References
- [`WKFocusedFormControlView.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L67)
- [`WKFocusedFormControlView.mm#L278`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L278)
- [`WKFocusedFormControlView.mm#L366`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L366)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
