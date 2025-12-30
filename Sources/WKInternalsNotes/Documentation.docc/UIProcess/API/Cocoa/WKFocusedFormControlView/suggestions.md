# ``WKInternalsNotes/WKFocusedFormControlView/suggestions``

表示可能な `UITextSuggestion` の配列を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<UITextSuggestion *> *suggestions;
```

## Default Value
初期値は `nil`。

## Discussion
setter は `displayText` を持つ候補だけを抽出して `_textSuggestions` を更新し、変更があれば delegate に通知する。

## References
- [`WKFocusedFormControlView.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L69)
- [`WKFocusedFormControlView.mm#L457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L457)
- [`WKFocusedFormControlView.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L462)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
