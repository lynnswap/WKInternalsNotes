# ``WKInternalsNotes/WKNumberPadViewController/inputMode``

数値入力モードを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKNumberPadInputMode inputMode;
```

## Default Value
初期化時に渡された `inputMode` を保持する。

## Discussion
`initWithDelegate:initialText:inputMode:` で設定された `_inputMode` を返す。

## References
- [`WKNumberPadViewController.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.h#L36)
- [`WKNumberPadViewController.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.mm#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
