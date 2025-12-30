# ``WKInternalsNotes/WKExtendedTextInputTraits/allowsNumberPadPopover``

ナンバーパッドのポップオーバー表示可否を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowsNumberPadPopover;
```

## Default Value
初期値は `NO`。

## Discussion
`init` と `restoreDefaultValues` の両方で `NO` に設定される。

## References
- [`WKExtendedTextInputTraits.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L66)
- [`WKExtendedTextInputTraits.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L49)
- [`WKExtendedTextInputTraits.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L141)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
