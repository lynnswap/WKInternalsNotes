# ``WKInternalsNotes/WKWebGeolocationPolicyDecider/decidePolicyForGeolocationRequestFromOrigin(_:requestingURL:view:listener:)``

Geolocation リクエストの許可/拒否判断を開始する。

## Objective-C Declaration
```objective-c
- (void)decidePolicyForGeolocationRequestFromOrigin:(const WebCore::SecurityOriginData&)securityOrigin requestingURL:(NSURL *)requestingURL view:(WKWebView *)view listener:(id<WKWebAllowDenyPolicyListener>)listener;
```

## Discussion
`securityOrigin` と `requestingURL`、`view`、`listener` を保持した `PermissionRequest` を作成し、内部キュー (`_challenges`) に追加したうえで `_executeNextChallenge` を呼び出す。`_executeNextChallenge` は履歴ファイルの読み込み後、テスト用のバイパスやチャレンジ回数の閾値を確認し、必要であれば UI アラートを提示して許可/拒否を確定する。

## References
- [`WKWebGeolocationPolicyDecider.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDecider.h#L42)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L144)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L146)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L151)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L158)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
