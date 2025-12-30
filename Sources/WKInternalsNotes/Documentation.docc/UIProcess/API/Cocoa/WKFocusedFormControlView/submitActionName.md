# ``WKInternalsNotes/WKFocusedFormControlView/submitActionName``

送信ボタンの表示名を保持し、ボタン表示を更新する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *submitActionName;
```

## Default Value
初期値は `nil`。

## Discussion
getter は `_submitActionName` を返す。setter は値が変わった場合に `_submitButton` の attributed title を更新し、`setNeedsLayout` を呼ぶ。

## References
- [`WKFocusedFormControlView.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L66)
- [`WKFocusedFormControlView.mm#L320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L320)
- [`WKFocusedFormControlView.mm#L330`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L330)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
