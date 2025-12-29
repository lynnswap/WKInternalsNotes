# ``WKInternalsNotes/_WKProcessPoolConfiguration/processSwapsOnNavigation``

ナビゲーション時のプロセススワップを有効/無効にする。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL processSwapsOnNavigation WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
既定値は `false`（クライアント未設定時は実験機能の値にフォールバック）。

## Discussion
setter は `setProcessSwapsOnNavigation` を設定し、getter は `processSwapsOnNavigation()` を返す。クライアントが未設定の場合は実験機能側の設定値が使われる。

## References
- [`_WKProcessPoolConfiguration.mm#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L236)
- [`_WKProcessPoolConfiguration.mm#L241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L241)
- [`APIProcessPoolConfiguration.h#L189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L189)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
