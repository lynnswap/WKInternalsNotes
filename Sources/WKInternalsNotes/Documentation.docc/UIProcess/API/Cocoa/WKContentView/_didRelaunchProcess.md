# ``WKInternalsNotes/WKContentView/_didRelaunchProcess()``

Webプロセス再起動後の初期化を行う。

## Objective-C Declaration
```objective-c
- (void)_didRelaunchProcess;
```

## Discussion
アクセシビリティトークンを再登録し、インタラクション設定と可視性伝播の再構成を行う。

## References
- [`WKContentView.h#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L106)
- [`WKContentView.mm#L939`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L939)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
