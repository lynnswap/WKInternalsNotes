# ``WKInternalsNotes/WKNumberPadViewController/didSelectKey(_:)``

キー入力を処理する。

## Objective-C Declaration
```objective-c
- (void)didSelectKey:(WKNumberPadKey)key;
```

## Discussion
`_handleKeyPress:` に委譲し、入力テキストや確定操作を処理する。

## References
- [`WKNumberPadViewController.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.h#L34)
- [`WKNumberPadViewController.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.mm#L139)
- [`WKNumberPadViewController.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadViewController.mm#L141)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
