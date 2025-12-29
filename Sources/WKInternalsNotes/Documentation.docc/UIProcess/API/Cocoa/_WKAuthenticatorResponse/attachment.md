# ``WKInternalsNotes/_WKAuthenticatorResponse/attachment``

認証器のアタッチメント種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKAuthenticatorAttachment attachment;
```

## Default Value
各初期化メソッドで渡された `attachment`。

## Discussion
初期化時に `_attachment` へ保存し、getter で返す。

## References
- [`_WKAuthenticatorResponse.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.h#L40)
- [`_WKAuthenticatorResponse.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
