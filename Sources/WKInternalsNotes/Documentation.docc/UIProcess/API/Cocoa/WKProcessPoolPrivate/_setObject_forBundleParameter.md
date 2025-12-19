# ``WKInternalsNotes/WKProcessPool/_setObject(_:forBundleParameter:)``

バンドルパラメータを 1 件設定する。

## Objective-C Declaration
```objective-c
- (void)_setObject:(id <NSCopying, NSSecureCoding>)object forBundleParameter:(NSString *)parameter;
```

## Discussion
object をコピーして secure coding でエンコードし、bundle parameters に追加/削除した後、`SetInjectedBundleParameter` を全プロセスへ送信する。

## References
- [`WKProcessPoolPrivate.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L90)
- [`WKProcessPool.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L262)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
