# ``WKInternalsNotes/_WKProcessPoolConfiguration/injectedBundleURL``

インジェクト用バンドルのファイル URL を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSURL *injectedBundleURL;
```

## Default Value
未設定時は空パス（`m_injectedBundlePath` が空）として扱われる。

## Discussion
getter は `injectedBundlePath` を `file://` URL に変換して返す。setter は file URL 以外を拒否して `NSInvalidArgumentException` を投げ、パスを `ProcessPoolConfiguration` に保存する。

## References
- [`_WKProcessPoolConfiguration.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L59)
- [`_WKProcessPoolConfiguration.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L64)
- [`APIProcessPoolConfiguration.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L176)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
