# ``WKInternalsNotes/WKNumberPadViewController/initWithDelegate(_:initialText:inputMode:)``

初期テキストと入力モードを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDelegate:(id <PUICQuickboardViewControllerDelegate>)delegate initialText:(NSString *)initialText inputMode:(WKNumberPadInputMode)inputMode;
```

## Discussion
`[super initWithDelegate:]` が成功した場合、`initialText` の可変コピーを保持し、`_inputMode` を設定する。`_shouldDismissWithFadeAnimation` は `NO` に初期化される。

## References
- [`WKNumberPadViewController.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.h#L33)
- [`WKNumberPadViewController.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.mm#L61)
- [`WKNumberPadViewController.mm#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.mm#L68)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
