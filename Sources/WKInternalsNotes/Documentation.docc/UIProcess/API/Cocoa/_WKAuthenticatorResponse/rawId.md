# ``WKInternalsNotes/_WKAuthenticatorResponse/rawId``

rawId のデータを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, readonly) NSData *rawId;
```

## Default Value
各初期化メソッドで渡された `rawId` を retain した値。

## Discussion
初期化時に `_rawId` を retain して保持し、getter で返す。

## References
- [`_WKAuthenticatorResponse.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.h#L42)
- [`_WKAuthenticatorResponse.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
