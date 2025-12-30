# ``WKInternalsNotes/WKExtendedTextInputTraits/secureTextEntry``

セキュア入力かどうかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isSecureTextEntry) BOOL secureTextEntry;
```

## Default Value
初期値は `NO`。

## Discussion
`restoreDefaultValues` で `NO` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L50)
- [`WKExtendedTextInputTraits.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L143)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
